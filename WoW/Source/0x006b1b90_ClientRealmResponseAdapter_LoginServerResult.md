---
offset: "0x006b1b90"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006b1b90 — `ClientRealmResponseAdapter_LoginServerResult`

- **Адрес (Offset):** `0x006b1b90`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/ClientServices.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006b1b90
void ClientRealmResponseAdapter::LoginServerResult(LOGIN_STATE state, LOGIN_RESULT result, const char* message1, const char* message2, const char* message3) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006b1b90 в IDA Pro / Ghidra
