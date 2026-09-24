# Muse 2.2 client flag registry

Extracted from `Muse.app/Contents/Resources/hatch/metaconfig.json` — Muse 2.2, build 1074644564, production channel. These are the flags the bundled web client knows about, with their parameter IDs. Client defaults live in the bundled JS (`Resources/hatch/index.html`); server-side values are not visible statically.

| parameter id | flag key | type |
|---|---|---|
| `c79e510b` | `hatch_config:hatch_big_boy_models` | boolean |
| `d72fa5a4` | `hatch_gtm:hatch_public_rollout_canada` | boolean |
| `2223e52e` | `hatch_gtm:invite_enabled` | boolean |
| `0de9ebf8` | `hatch_gtm:redeem_invite_enabled` | boolean |
| `5741bfe7` | `hatch_web:android_alpha_group_uri` | string |
| `06737e88` | `hatch_web:android_alpha_play_store_uri` | string |
| `7242d327` | `hatch_web:attestation_enforce_mode` | number |
| `5e1fb489` | `hatch_web:ecto1_is_employee` | boolean |
| `05344cb9` | `hatch_web:ecto1_redteaming` | boolean |
| `49572c1a` | `hatch_web:enable_dictation_asr_streaming` | boolean |
| `ceb5881a` | `hatch_web:enable_idea_color_icons` | boolean |
| `788be016` | `hatch_web:enable_surveys` | boolean |
| `8830de59` | `hatch_web:falco_qpl_transport` | string |
| `4398b639` | `hatch_web:hatch_acs_ohai_enabled` | boolean |
| `e75238b7` | `hatch_web:hatch_alpha_cohort` | boolean |
| `dde7768a` | `hatch_web:hatch_channel_messenger_enabled` | boolean |
| `c6e95b18` | `hatch_web:hatch_channel_telegram_enabled` | boolean |
| `6fb3f373` | `hatch_web:hatch_channel_whatsapp_enabled` | boolean |
| `4b23af6e` | `hatch_web:hatch_delegates_web` | boolean |
| `d01136f4` | `hatch_web:hatch_feed_infinite_scroll_enabled_gk` | boolean |
| `7402e958` | `hatch_web:hatch_link_enabled` | boolean |
| `1d23e303` | `hatch_web:hatch_macos_download_link_gating` | boolean |
| `e76b2a1d` | `hatch_web:hatch_phone_live_transcript_enabled` | boolean |
| `1722f13b` | `hatch_web:hatch_reset_vm` | boolean |
| `e3507fea` | `hatch_web:hatch_subscription_enabled` | boolean |
| `7b2653e9` | `hatch_web:hatch_use_ccv_redirect` | boolean |
| `572a7c97` | `hatch_web:hatch_voice_feat` | boolean |
| `9cd8f8f3` | `hatch_web:hatch_voice_id` | string |
| `df110356` | `hatch_web:hatch_web_cvm` | boolean |
| `34adca57` | `hatch_web:hatch_whitehat_cohort` | boolean |
| `f9ea7727` | `hatch_web:hatch_work_oidc_authentication` | boolean |
| `052386ec` | `hatch_web:ios_app_store_uri` | string |
| `11306b54` | `hatch_web:ios_testflight_uri` | string |
| `a243b541` | `hatch_web:is_debug_build` | boolean |
| `83580e32` | `hatch_web:is_tool_mocking_enabled_for_hatch` | boolean |
| `ed3fe1bb` | `hatch_web:map_political_view` | string |
| `bb0fb6dd` | `hatch_web:map_vector_style_dark` | string |
| `249b5159` | `hatch_web:map_vector_style_light` | string |
| `5325d097` | `hatch_web:muse_mail` | boolean |
| `9cb0727d` | `hatch_web:ptt_skip_certs_verification_by_payment_env` | boolean |
| `f1805006` | `hatch_web:skip_nux_to_pux_transition` | boolean |
| `75f09f6a` | `hatch_web:subs_employee_hatch_lower_price` | boolean |
| `a8da3436` | `hatch_web:whatsapp_settings_learn_more_url` | string |
| `a145793f` | `mwa_help_and_support:hatch_support_web_april_launch` | boolean |

Total: 44 flags.
