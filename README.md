# 拾光｜個人學習行程與任務管理系統

拾光是一套響應式個人學習規劃網頁，使用 Firebase Authentication 提供 Google 登入，並支援今日學習、週行程與所有任務工作區。

## 功能

- Firebase Authentication Google 帳戶登入／登出
- 依 Firebase 使用者 UID 隔離本機任務資料
- 今日學習清單、週行程總覽與所有任務篩選
- 任務新增／編輯：科目、優先級、學習日期、截止日、時間、估時、備註與完成狀態
- localStorage 儲存（每個登入帳戶在同一瀏覽器使用獨立資料空間）
- 桌機側欄與手機底部導覽

## Firebase 設定

### 1. 建立 Firebase Web App

在 [Firebase Console](https://console.firebase.google.com/) 建立或選取專案，新增 Web App，複製 SDK 設定中的 `apiKey`、`authDomain`、`projectId`、`appId`。

### 2. 啟用 Google 登入

Firebase Console → Authentication → Sign-in method → 啟用 Google。若要限制登入者，可在 Authentication 的使用者／存取政策中另行設定。

### 3. 設定前端設定檔

複製 `firebase-config.example.js` 為 `firebase-config.js`，填入 Firebase Console 的 Web App 設定值。`firebase-config.js` 已列入 `.gitignore`，不會提交到 Git。

### 4. 加入授權網域

Firebase Console → Authentication → Settings → Authorized domains，加入網站實際使用的網域。例如 GitHub Pages 部署時加入 `6dk4wytb77-ux.github.io`。本機測試建議透過 localhost 網頁伺服器，而不是直接開啟 `file://`。

### 5. 啟動

以 localhost 或部署網站提供靜態檔案，開啟 `index.html`。此原型使用瀏覽器 ES Modules 與 Firebase CDN SDK，必須透過 HTTP(S) 來源執行。

## 資料與安全

目前 Firebase 僅負責身分驗證。任務仍存於目前瀏覽器的 localStorage，並依登入 UID 命名空間隔離；清除瀏覽器資料或換裝置不會自動同步。若需雲端同步，後續須接入 Firestore，並配置以 `request.auth.uid` 為依據的安全規則。

Firebase Web App 設定中的 API key 是用於識別 Firebase 專案，不是伺服器管理憑證；但應限制 API key 的可用 API／來源。絕不可將 Admin SDK 私鑰、服務帳號憑證或其他伺服器秘密放入前端。

## 專案檔案

- `index.html`：登入畫面與應用頁面
- `app.js`：Firebase Auth、工作區互動與本機任務保存
- `firebase-config.example.js`：Firebase 設定檔範本
- `firebase-config.js`：本機設定檔（自行建立，不提交）
- `styles.css`：響應式樣式
- `PRD_個人學習行程與任務管理系統.docx`：產品需求文件
