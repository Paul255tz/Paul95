# Paul Mndeme: Android app

An Android app that shows the website in [`../index.html`](../index.html),
including both versions of Episode 1. Everything is bundled inside the app, so
the videos play offline.

## Get the APK

Every push that changes the app or the website builds it on GitHub Actions:

1. Open the repo's **Actions** tab and pick the latest **Android app** run.
2. Download the **paul-mndeme-app** artifact and unzip it to get `app-debug.apk`.
3. Copy it to your phone and open it. Android will ask you to allow installs
   from that source the first time.

## Build it yourself

Open this `android/` folder in Android Studio, or run:

```bash
./gradlew assembleDebug   # APK lands in app/build/outputs/apk/debug/
```

The build copies `index.html` and the episode videos from the repo root into
the app, so edit the website there and rebuild.
