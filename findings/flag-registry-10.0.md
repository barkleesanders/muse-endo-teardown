# Muse 10.0 client flag registry

Build 1103401639, production channel. DMG SHA-256: `af1aea5cfb2903fa651358eaadef5dc443b6396e5e020f13bcd7b8689d81f796`.
Source: `Muse.app/Contents/Resources/hatch/metaconfig.json`.
Client defaults live in the bundled JS; server-side values are not
visible statically — see the /decompile skill ground-truth rule.

| parameter id | flag key | type |
|---|---|---|
| `c79e510b` | `hatch_config:hatch_big_boy_models` | boolean |
| `b8dbdcb0` | `hatch_desktop:show_subscription_usage_on_cvm` | boolean |
| `8c1233db` | `hatch_gtm:hatch_us_pjs` | boolean |
| `2223e52e` | `hatch_gtm:invite_enabled` | boolean |
| `0de9ebf8` | `hatch_gtm:redeem_invite_enabled` | boolean |
| `7242d327` | `hatch_web:attestation_enforce_mode` | number |
| `57ee1519` | `hatch_web:cvm_chip_allowlist_max_age_hours` | number |
| `dccdcd94` | `hatch_web:cvm_hard_replacement_enabled` | boolean |
| `2d5df86d` | `hatch_web:delete_svm_during_cvm_upgrade` | boolean |
| `5e1fb489` | `hatch_web:ecto1_is_employee` | boolean |
| `05344cb9` | `hatch_web:ecto1_redteaming` | boolean |
| `49572c1a` | `hatch_web:enable_dictation_asr_streaming` | boolean |
| `ceb5881a` | `hatch_web:enable_idea_color_icons` | boolean |
| `788be016` | `hatch_web:enable_surveys` | boolean |
| `fab1356c` | `hatch_web:hatch_1password_integration` | boolean |
| `6d51a173` | `hatch_web:hatch_1password_manual_grant` | boolean |
| `4398b639` | `hatch_web:hatch_acs_ohai_enabled` | boolean |
| `dde7768a` | `hatch_web:hatch_channel_messenger_enabled` | boolean |
| `c6e95b18` | `hatch_web:hatch_channel_telegram_enabled` | boolean |
| `6fb3f373` | `hatch_web:hatch_channel_whatsapp_enabled` | boolean |
| `d01136f4` | `hatch_web:hatch_feed_infinite_scroll_enabled_gk` | boolean |
| `7402e958` | `hatch_web:hatch_link_enabled` | boolean |
| `8a7e4e16` | `hatch_web:hatch_login_provider_support` | boolean |
| `1d23e303` | `hatch_web:hatch_macos_download_link_gating` | boolean |
| `e76b2a1d` | `hatch_web:hatch_phone_live_transcript_enabled` | boolean |
| `1722f13b` | `hatch_web:hatch_reset_vm` | boolean |
| `e3507fea` | `hatch_web:hatch_subscription_enabled` | boolean |
| `a99a7081` | `hatch_web:hatch_tasks_list_redesign` | boolean |
| `7b2653e9` | `hatch_web:hatch_use_ccv_redirect` | boolean |
| `2b9f95c3` | `hatch_web:hatch_virtual_tryon_enabled` | boolean |
| `7951eeff` | `hatch_web:hatch_voice_design_enabled` | boolean |
| `2975fa50` | `hatch_web:hatch_voice_embodiment_enabled` | boolean |
| `572a7c97` | `hatch_web:hatch_voice_feat` | boolean |
| `9cd8f8f3` | `hatch_web:hatch_voice_id` | string |
| `df110356` | `hatch_web:hatch_web_cvm` | boolean |
| `34adca57` | `hatch_web:hatch_whitehat_cohort` | boolean |
| `f9ea7727` | `hatch_web:hatch_work_oidc_authentication` | boolean |
| `26ca296d` | `hatch_web:home_device_help_url` | string |
| `d045ad6c` | `hatch_web:home_link_claim_enabled` | boolean |
| `052386ec` | `hatch_web:ios_app_store_uri` | string |
| `a243b541` | `hatch_web:is_debug_build` | boolean |
| `83580e32` | `hatch_web:is_tool_mocking_enabled_for_hatch` | boolean |
| `ed3fe1bb` | `hatch_web:map_political_view` | string |
| `bb0fb6dd` | `hatch_web:map_vector_style_dark` | string |
| `56bbe4c9` | `hatch_web:map_vector_style_grayscale` | string |
| `249b5159` | `hatch_web:map_vector_style_light` | string |
| `5325d097` | `hatch_web:muse_mail` | boolean |
| `9cb0727d` | `hatch_web:ptt_skip_certs_verification_by_payment_env` | boolean |
| `515d44c2` | `hatch_web:redteam_log_modal` | boolean |
| `0ac08bc5` | `hatch_web:show_whatsapp_on_cvm` | boolean |
| `f1805006` | `hatch_web:skip_nux_to_pux_transition` | boolean |
| `75f09f6a` | `hatch_web:subs_employee_hatch_lower_price` | boolean |
| `a8da3436` | `hatch_web:whatsapp_settings_learn_more_url` | string |
| `f5a0bdf7` | `hatch_web_sessionless:enable_passkey_login` | boolean |
| `1145b8a6` | `hatch_web_sessionless:one_tap_login_killswitch` | boolean |
| `a145793f` | `mwa_help_and_support:hatch_support_web_april_launch` | boolean |

Total: 56 flags.
