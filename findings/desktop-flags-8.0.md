# Muse 8.0 native binary findings

Build 1093405488. Extracted via `strings` on `Contents/MacOS/Muse`.
These are string references, not proof of behavior.

## hatch_desktop flags (20)
- `hatch_desktop:attestation_enforce_mode`
- `hatch_desktop:dictation_backend`
- `hatch_desktop:disable_external_dictation_zdr`
- `hatch_desktop:enable_browser_automation`
- `hatch_desktop:enable_computer_control`
- `hatch_desktop:enable_dictation_analytics`
- `hatch_desktop:enable_dictation_language_bias`
- `hatch_desktop:enable_dictation_rewrite`
- `hatch_desktop:enable_media_to_cosmos`
- `hatch_desktop:enable_pre_connect_dictation`
- `hatch_desktop:enable_ptt_s2s`
- `hatch_desktop:enable_voice_mode`
- `hatch_desktop:endo_block_files_commands`
- `hatch_desktop:endo_blocked_apps_enabled`
- `hatch_desktop:endo_enable_computer_use_onboarding`
- `hatch_desktop:endo_enable_screen_recording`
- `hatch_desktop:voyager_dictation_endpoint`
- `hatch_desktop:voyager_dictation_model`
- `hatch_desktop:voyager_dictation_use_abra_auth`
- `hatch_desktop:voyager_is_employee`

## hatch_web flags (8)
- `hatch_web:attestation_enforce_mode`
- `hatch_web:cvm_hard_replacement_enabled`
- `hatch_web:ecto1_is_employee`
- `hatch_web:hatch_acs_ohai_enabled`
- `hatch_web:hatch_activation`
- `hatch_web:hatch_web_cvm`
- `hatch_web:is_debug_build`
- `hatch_web:show_whatsapp_on_cvm`

## config/cache refs (0)
- (none found)

## mobileconfig refs (26)
- `//meta.graph.meta.com/mobileconfigsessionless`
- `Endo/MobileConfigClient.swift`
- `EndoMobileConfigClient`
- `FBMobileConfigStartupConfigs`
- `FBMobileConfigStartupConfigsDeprecated`
- `FBMobileConfigStartupConfigsOverride`
- `MobileConfig`
- `MobileConfig.`
- `MobileConfigDebugView`
- `MobileConfigError`
- `MobileConfigSnapshot`
- `MobileConfigValue`
- `QMobileConfigSocket_`
- `SharedMobileConfigClient`
- `SharedMobileConfigClient.current`
- `TMobileConfigSocket_`
- `_FBMobileConfigStartupConfigsDeprecated`
- `_FBSQLMobileConfigSocket_GetPlugin`
- `_FBSQLMobileConfigSocket_InvokeGetEnabled`
- `_MobileConfigInitOverrideDefaultKeyForMcConfigsSocket_GetPlugin`
- `_TtC4Endo22EndoMobileConfigClient`
- `_TtC4Endo24SharedMobileConfigClient`
- `_mobileConfig`
- `com.meta.endo/MobileConfig`
- `mobileConfig`
- `mobileconfig.override.`
