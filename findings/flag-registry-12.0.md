# Muse 12.0 client flag registry

Build 1113521811, production channel. DMG SHA-256: `d2fb78b9368e88bdcef06112ec65e9f07d8fae25ac3ac67cc2c814f6842e4d6d`.
Source: `Muse.app/Contents/Resources/hatch/metaconfig.json`.
Client defaults live in the bundled JS; server-side values are not
visible statically — see the /decompile skill ground-truth rule.

| parameter id | flag key | type |
|---|---|---|
| `1d2f0705` | `endo_rollout:chrome_extension_upsell_auto_show_enabled` | boolean |
| `91fce8e6` | `endo_rollout:chrome_extension_upsell_enabled` | boolean |
| `c79e510b` | `hatch_config:hatch_big_boy_models` | boolean |
| `b8dbdcb0` | `hatch_desktop:show_subscription_usage_on_cvm` | boolean |
| `8c1233db` | `hatch_gtm:hatch_us_pjs` | boolean |
| `2223e52e` | `hatch_gtm:invite_enabled` | boolean |
| `0de9ebf8` | `hatch_gtm:redeem_invite_enabled` | boolean |
| `7242d327` | `hatch_web:attestation_enforce_mode` | number |
| `dccdcd94` | `hatch_web:cvm_hard_replacement_enabled` | boolean |
| `ad1c3ebc` | `hatch_web:cvm_upgrade_downgrade_migrate_option_enabled` | boolean |
| `2d5df86d` | `hatch_web:delete_svm_during_cvm_upgrade` | boolean |
| `5e1fb489` | `hatch_web:ecto1_is_employee` | boolean |
| `05344cb9` | `hatch_web:ecto1_redteaming` | boolean |
| `49572c1a` | `hatch_web:enable_dictation_asr_streaming` | boolean |
| `ceb5881a` | `hatch_web:enable_idea_color_icons` | boolean |
| `788be016` | `hatch_web:enable_surveys` | boolean |
| `fab1356c` | `hatch_web:hatch_1password_integration` | boolean |
| `6d51a173` | `hatch_web:hatch_1password_manual_grant` | boolean |
| `d5439438` | `hatch_web:hatch_avatar_assets_api` | boolean |
| `dde7768a` | `hatch_web:hatch_channel_messenger_enabled` | boolean |
| `c6e95b18` | `hatch_web:hatch_channel_telegram_enabled` | boolean |
| `6fb3f373` | `hatch_web:hatch_channel_whatsapp_enabled` | boolean |
| `d01136f4` | `hatch_web:hatch_feed_infinite_scroll_enabled_gk` | boolean |
| `7402e958` | `hatch_web:hatch_link_enabled` | boolean |
| `8a7e4e16` | `hatch_web:hatch_login_provider_support` | boolean |
| `1d23e303` | `hatch_web:hatch_macos_download_link_gating` | boolean |
| `2073def8` | `hatch_web:hatch_multi_login_support` | boolean |
| `3acd24d9` | `hatch_web:hatch_pdp_save_button` | boolean |
| `e76b2a1d` | `hatch_web:hatch_phone_live_transcript_enabled` | boolean |
| `4010d8dc` | `hatch_web:hatch_place_save_button` | boolean |
| `1722f13b` | `hatch_web:hatch_reset_vm` | boolean |
| `e3507fea` | `hatch_web:hatch_subscription_enabled` | boolean |
| `a99a7081` | `hatch_web:hatch_tasks_list_redesign` | boolean |
| `478c8c5a` | `hatch_web:hatch_voice_announcement_body_variant` | string |
| `4a47b38e` | `hatch_web:hatch_voice_announcement_enabled` | boolean |
| `79f09896` | `hatch_web:hatch_voice_announcement_variant` | string |
| `2d937af9` | `hatch_web:hatch_voice_avatar_switching_enabled` | boolean |
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
| `599f2b00` | `hatch_web:muse_shopping_tryon_eligibility_in_pdp_enable` | boolean |
| `9cb0727d` | `hatch_web:ptt_skip_certs_verification_by_payment_env` | boolean |
| `0ac08bc5` | `hatch_web:show_whatsapp_on_cvm` | boolean |
| `f1805006` | `hatch_web:skip_nux_to_pux_transition` | boolean |
| `2f833ce7` | `hatch_web:spaces_enabled` | boolean |
| `75f09f6a` | `hatch_web:subs_employee_hatch_lower_price` | boolean |
| `a8da3436` | `hatch_web:whatsapp_settings_learn_more_url` | string |
| `f5a0bdf7` | `hatch_web_sessionless:enable_passkey_login` | boolean |
| `1145b8a6` | `hatch_web_sessionless:one_tap_login_killswitch` | boolean |
| `a145793f` | `mwa_help_and_support:hatch_support_web_april_launch` | boolean |

Total: 63 flags.
