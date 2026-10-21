---
offset: "0x00465480"
module: "WoW/Source"
file: "WoW/Source/WowServices/Login.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00465480 — `LoginResponse_UpdateLoginStatus`

- **Адрес (Offset):** `0x00465480`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/Login.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00465480
void LoginResponse::UpdateLoginStatus(LOGIN_STATE state, LOGIN_RESULT result, const char* addressString, uint16_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00465480 в IDA Pro / Ghidra
