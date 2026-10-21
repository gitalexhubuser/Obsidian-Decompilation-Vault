---
offset: "0x008c5e30"
module: "WoW/Source"
file: "WoW/Source/WowServices/BattlenetLogin.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008c5e30 — `BattlenetLogin_GetMatrixInfo`

- **Адрес (Offset):** `0x008c5e30`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/BattlenetLogin.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008c5e30
bool BattlenetLogin::GetMatrixInfo(uint32_t* width, uint32_t* height, uint32_t* minDigits, uint32_t* maxDigits, bool* flipCoords, uint32_t* challengeCount) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008c5e30 в IDA Pro / Ghidra
