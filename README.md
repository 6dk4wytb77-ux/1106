# 拾光｜個人學習行程與任務管理系統

拾光是一套響應式個人學習規劃網頁，使用 Firebase Authentication 提供 Google 登入，支援今日學習、週行程與所有任務工作區。

## GitHub Pages

此儲存庫使用 GitHub Actions 自動部署 Pages。推送到 `main` 後會執行 `.github/workflows/pages.yml`。首次啟用請至 GitHub 儲存庫 **Settings → Pages → Build and deployment → Source** 選擇 **GitHub Actions**。部署完成後，專案網站網址為：

<https://6dk4wytb77-ux.github.io/1106/>

## Firebase Google 登入設定

1. 在 [Firebase Console](https://console.firebase.google.com/) 建立或選取 Firebase 專案並新增 Web App。
2. 到 **Authentication → Sign-in method** 啟用 **Google**。
3. 複製 `firebase-config.example.js` 為 `firebase-config.js`，填入 Firebase Web App 的 `apiKey`、`authDomain`、`projectId`、`appId`。設定檔已加入 `.gitignore`。
4. 到 **Authentication → Settings → Authorized domains** 加入 `6dk4wytb77-ux.github.io`。
5. 在本機建置／發佈流程中提供 `firebase-config.js`。該檔案不提交至版本庫。

若尚未設定 Firebase，Pages 網站仍會開啟並顯示設定提示，但登入按鈕會停用。

## 功能

- Google 帳戶登入與登出
- 以 Firebase UID 區隔每個登入者的瀏覽器本機資料
- 今日學習、週行程與所有任務工作區
- 新增／編輯學習任務：科目、優先順序、學習日期、截止日、時段、預估時間、備註
- localStorage 保存任務及科目
- 桌機與手機響應式版面

## 資料保存說明

Firebase 目前僅用於身份驗證，任務資料仍保存在目前瀏覽器的 localStorage，不會跨裝置同步。正式提供服務前，請另行設計 Firestore 權限規則與備份策略。
