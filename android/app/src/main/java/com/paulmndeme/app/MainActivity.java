package com.paulmndeme.app;

import android.app.Activity;
import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.content.res.AssetFileDescriptor;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.view.WindowInsets;
import android.webkit.WebChromeClient;
import android.webkit.WebResourceRequest;
import android.webkit.WebResourceResponse;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.FrameLayout;

import java.io.FilterInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.HashMap;
import java.util.Map;

/** Shows the website bundled in assets/site/ in a full-screen WebView. */
public class MainActivity extends Activity {

    // Bundled files are served from this https origin so the page behaves like a normal website.
    private static final String HOST = "appassets.androidplatform.net";
    private static final String START_URL = "https://" + HOST + "/site/index.html";

    private FrameLayout root;
    private WebView web;
    private View fullscreenView;
    private WebChromeClient.CustomViewCallback fullscreenCallback;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        root = new FrameLayout(this);
        web = new WebView(this);
        root.addView(web);
        setContentView(root);

        // Keep the page clear of the status and navigation bars (edge-to-edge on Android 15+).
        root.setOnApplyWindowInsetsListener((v, insets) -> {
            if (fullscreenView == null) {
                v.setPadding(insets.getSystemWindowInsetLeft(), insets.getSystemWindowInsetTop(),
                        insets.getSystemWindowInsetRight(), insets.getSystemWindowInsetBottom());
            } else {
                v.setPadding(0, 0, 0, 0);
            }
            return insets;
        });

        WebSettings settings = web.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true);
        settings.setMediaPlaybackRequiresUserGesture(true);

        web.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
                Uri uri = request.getUrl();
                if (HOST.equals(uri.getHost())) {
                    return false;
                }
                // Links to other sites (GitHub, email) open in the right app.
                try {
                    startActivity(new Intent(Intent.ACTION_VIEW, uri));
                } catch (ActivityNotFoundException ignored) {
                }
                return true;
            }

            @Override
            public WebResourceResponse shouldInterceptRequest(WebView view, WebResourceRequest request) {
                Uri uri = request.getUrl();
                if (!HOST.equals(uri.getHost()) || uri.getPath() == null) {
                    return null;
                }
                return serveAsset(uri.getPath().substring(1), request.getRequestHeaders());
            }
        });

        web.setWebChromeClient(new WebChromeClient() {
            @Override
            public void onShowCustomView(View view, CustomViewCallback callback) {
                if (fullscreenView != null) {
                    callback.onCustomViewHidden();
                    return;
                }
                fullscreenView = view;
                fullscreenCallback = callback;
                root.addView(view, new FrameLayout.LayoutParams(
                        FrameLayout.LayoutParams.MATCH_PARENT, FrameLayout.LayoutParams.MATCH_PARENT));
                web.setVisibility(View.GONE);
                setFullscreenUi(true);
            }

            @Override
            public void onHideCustomView() {
                exitFullscreen();
            }
        });

        if (savedInstanceState != null) {
            web.restoreState(savedInstanceState);
        } else {
            web.loadUrl(START_URL);
        }
    }

    private void exitFullscreen() {
        if (fullscreenView == null) {
            return;
        }
        root.removeView(fullscreenView);
        fullscreenView = null;
        web.setVisibility(View.VISIBLE);
        setFullscreenUi(false);
        if (fullscreenCallback != null) {
            fullscreenCallback.onCustomViewHidden();
            fullscreenCallback = null;
        }
    }

    @SuppressWarnings("deprecation")
    private void setFullscreenUi(boolean on) {
        View decor = getWindow().getDecorView();
        decor.setSystemUiVisibility(on
                ? View.SYSTEM_UI_FLAG_FULLSCREEN | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
                        | View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY | View.SYSTEM_UI_FLAG_LAYOUT_STABLE
                : View.SYSTEM_UI_FLAG_VISIBLE);
        root.requestApplyInsets();
    }

    /** Serves a file from assets/, answering HTTP Range requests so videos can seek. */
    private WebResourceResponse serveAsset(String path, Map<String, String> requestHeaders) {
        String mime = mimeType(path);
        Map<String, String> headers = new HashMap<>();
        try {
            if (!path.endsWith(".mp4")) {
                return new WebResourceResponse(mime, mime.startsWith("text/") ? "utf-8" : null,
                        200, "OK", headers, getAssets().open(path));
            }

            AssetFileDescriptor fd = getAssets().openFd(path);
            long length = fd.getLength();
            long start = 0;
            long end = length - 1;
            String range = null;
            for (Map.Entry<String, String> h : requestHeaders.entrySet()) {
                if ("range".equalsIgnoreCase(h.getKey())) {
                    range = h.getValue();
                }
            }
            boolean partial = range != null && range.startsWith("bytes=");
            if (partial) {
                String[] parts = range.substring(6).split(",")[0].trim().split("-", -1);
                if (!parts[0].isEmpty()) {
                    start = Long.parseLong(parts[0]);
                    if (parts.length > 1 && !parts[1].isEmpty()) {
                        end = Math.min(Long.parseLong(parts[1]), length - 1);
                    }
                } else if (parts.length > 1 && !parts[1].isEmpty()) {
                    start = Math.max(0, length - Long.parseLong(parts[1]));
                }
                if (start > end) {
                    fd.close();
                    headers.put("Content-Range", "bytes */" + length);
                    return new WebResourceResponse(mime, null, 416, "Range Not Satisfiable", headers, null);
                }
            }

            InputStream in = fd.createInputStream();
            long skipped = 0;
            while (skipped < start) {
                long n = in.skip(start - skipped);
                if (n <= 0) {
                    break;
                }
                skipped += n;
            }
            long count = end - start + 1;
            headers.put("Accept-Ranges", "bytes");
            headers.put("Content-Length", String.valueOf(count));
            if (partial) {
                headers.put("Content-Range", "bytes " + start + "-" + end + "/" + length);
            }
            return new WebResourceResponse(mime, null, partial ? 206 : 200,
                    partial ? "Partial Content" : "OK", headers, new LimitedInputStream(in, count));
        } catch (IOException | NumberFormatException e) {
            return new WebResourceResponse("text/plain", "utf-8", 404, "Not Found", headers, null);
        }
    }

    private static String mimeType(String path) {
        if (path.endsWith(".html")) return "text/html";
        if (path.endsWith(".css")) return "text/css";
        if (path.endsWith(".js")) return "text/javascript";
        if (path.endsWith(".mp4")) return "video/mp4";
        if (path.endsWith(".png")) return "image/png";
        if (path.endsWith(".jpg") || path.endsWith(".jpeg")) return "image/jpeg";
        if (path.endsWith(".svg")) return "image/svg+xml";
        return "application/octet-stream";
    }

    /** Reads at most {@code remaining} bytes from the wrapped stream. */
    private static final class LimitedInputStream extends FilterInputStream {
        private long remaining;

        LimitedInputStream(InputStream in, long remaining) {
            super(in);
            this.remaining = remaining;
        }

        @Override
        public int read() throws IOException {
            if (remaining <= 0) return -1;
            int b = super.read();
            if (b >= 0) remaining--;
            return b;
        }

        @Override
        public int read(byte[] b, int off, int len) throws IOException {
            if (remaining <= 0) return -1;
            int n = super.read(b, off, (int) Math.min(len, remaining));
            if (n > 0) remaining -= n;
            return n;
        }

        @Override
        public int available() throws IOException {
            return (int) Math.min(super.available(), remaining);
        }
    }

    @Override
    public void onBackPressed() {
        if (fullscreenView != null) {
            exitFullscreen();
        } else if (web.canGoBack()) {
            web.goBack();
        } else {
            super.onBackPressed();
        }
    }

    @Override
    protected void onSaveInstanceState(Bundle outState) {
        super.onSaveInstanceState(outState);
        web.saveState(outState);
    }

    @Override
    protected void onPause() {
        web.onPause();
        super.onPause();
    }

    @Override
    protected void onResume() {
        super.onResume();
        web.onResume();
    }

    @Override
    protected void onDestroy() {
        web.destroy();
        super.onDestroy();
    }
}
