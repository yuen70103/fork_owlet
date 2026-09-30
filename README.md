# Owlet Custom Integration

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]

[![License][license-shield]][license]

[![hacs][hacsbadge]][hacs]
[![Project Maintenance][maintenance-shield]][user_profile]

A custom component for the Owlet smart sock

## Installation

### HACS（推薦）

這是 `yuen70103/fork_owlet` fork，請用 HACS 的「自訂儲存庫」加入，不要只搜尋上游的 `Owlet`：

1. 在 Home Assistant 開啟 `HACS` → `Integrations`。
2. 點右上角 `⋮` → `Custom repositories`。
3. Repository 填入 `https://github.com/yuen70103/fork_owlet`，Category 選 `Integration`，按 `Add`。
4. 回到整合搜尋 `Owlet`，選取此 fork 後按 `Download`。
5. 重新啟動 Home Assistant。
6. 開啟 `Settings` → `Devices & services` → `+ Add Integration`，搜尋 `Owlet Smart Sock`。
7. 選擇 Owlet 帳號所在的 API region（`Europe` 或 `World`），輸入 Owlet 帳號電子郵件與密碼，完成設定。
8. 在新建立的 Owlet 裝置頁確認心率、血氧、電量等 entities 已出現。

此整合會依 manifest 自動安裝相容的 `pyowletapi==2025.4.10`，不需要另外 clone 或安裝 `fork_pyowletapi`。

### 手動安裝

適合沒有使用 HACS，或需要直接測試此 fork 的情況：

1. 在可存取 GitHub 的電腦下載此 repository，或執行：

   ```bash
   git clone https://github.com/yuen70103/fork_owlet.git
   ```

2. 找到 Home Assistant 的設定目錄（包含 `configuration.yaml` 的目錄）。
3. 將 repository 內的 `custom_components/owlet` 整個資料夾複製到設定目錄的 `custom_components/owlet`：

   ```text
   <HA config>/custom_components/owlet/
   ```

   若 `custom_components` 不存在，請先建立它；不要只複製 `manifest.json`。
4. 重新啟動 Home Assistant。
5. 依照上方第 6–8 步，在 UI 新增 `Owlet Smart Sock` 整合。

### 更新與移除

- HACS 安裝：在 HACS 的此 repository 頁面按 `Update`，再重新啟動 Home Assistant。
- 手動安裝：從 repository 取得最新檔案，完整替換 `<HA config>/custom_components/owlet/` 後重新啟動；請保留同一個資料夾名稱。
- 移除前先到 `Settings` → `Devices & services` 刪除 Owlet config entry，再刪除 component 資料夾並重新啟動。

### 常見問題

- 顯示找不到裝置：確認 region、Owlet 登入帳號及密碼正確；同一帳號若在不同 API region 使用，請建立不同的 config entry 並選擇正確 region。
- 登入後資料過期或讀不到：先到 `Settings` → `System` → `Logs` 查看 `owlet` 相關錯誤，確認 Home Assistant 能連線到 Owlet cloud service。
- 更新後設定流程無法載入：確認舊版 component 已完整移除、重新啟動過 Home Assistant，且沒有同時放置另一份 `custom_components/owlet`。
- 不要把 Owlet 密碼寫入 YAML、shell history 或公開 issue；請只在 Home Assistant 的設定流程輸入。


<!---->

## Usage

The `Owlet` integration offers integration with the Owlet Smart Sock cloud service. This provides sensors such as heart rate, oxygen saturation, charge percentage.

This integration provides the following entities:

- Binary sensors - charging status, high heart rate alert, low heart rate alert, high oxygen alert, low oxygen alert, low battery alert, lost power alert, sock diconnected alert, and sock status.
- Sensors - battery level, oxygen saturation, oxygen saturation 10 minute average, heart rate, battery time remaining, signal strength, and skin temperature.

## Options

- Seconds between polling - Number of seconds between each call for data from the owlet cloud service, default is 5 seconds.

---

[commits-shield]: https://img.shields.io/github/commit-activity/w/ryanbdclark/owlet?style=for-the-badge
[commits]: https://github.com/ryanbdclark/owlet/commits/main
[hacs]: https://github.com/hacs/integration
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[license]: LICENSE
[license-shield]: https://img.shields.io/github/license/ryanbdclark/owlet.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Ryan%20Clark%20%40ryanbdclark-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/ryanbdclark/owlet.svg?style=for-the-badge
[releases]: https://github.com/ryanbdclark/owlet/releases
[user_profile]: https://github.com/ryanbdclark
[add-integration]: https://my.home-assistant.io/redirect/config_flow_start?domain=owlet
[add-integration-badge]: https://my.home-assistant.io/badges/config_flow_start.svg
