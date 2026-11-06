# Copy this template into the Pages build output as firebase-config.js only
# for a Pages deployment that has not been provided Firebase config.
# This allows the published site to load and present the setup message,
# while keeping Google login disabled until real Firebase values are configured.
export const firebaseConfig = {
  apiKey: "REPLACE_WITH_FIREBASE_API_KEY",
  authDomain: "REPLACE_WITH_PROJECT.firebaseapp.com",
  projectId: "REPLACE_WITH_PROJECT_ID",
  appId: "REPLACE_WITH_FIREBASE_APP_ID"
};
