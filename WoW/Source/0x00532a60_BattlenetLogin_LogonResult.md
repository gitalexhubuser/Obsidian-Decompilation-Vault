---
offset: "0x00532a60"
module: "WoW/Source"
file: "WoW/Source/WowServices/BattlenetLogin.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00532a60 — `BattlenetLogin_LogonResult`

- **Адрес (Offset):** `0x00532a60`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/BattlenetLogin.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00532a60
void BattlenetLogin::LogonResult(Grunt::Result result, const uint8_t* sessionKey, uint32_t sessionKeyLength, uint16_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00532a60 в IDA Pro / Ghidra
