---
offset: "0x00532a60"
module: "WoW/Source"
file: "WoW/Source/WowServices/BattlenetLogin.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00532a60 — `BattlenetLogin_GetPinInfo`

- **Адрес (Offset):** `0x00532a60`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/BattlenetLogin.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00532a60
void BattlenetLogin::GetPinInfo(bool* enabled, uint8_t** salt, uint8_t** hash) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00532a60 в IDA Pro / Ghidra
