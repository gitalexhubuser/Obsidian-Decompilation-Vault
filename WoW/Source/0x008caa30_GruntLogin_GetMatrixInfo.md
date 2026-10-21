---
offset: "0x008caa30"
module: "WoW/Source"
file: "WoW/Source/WowServices/GruntLogin.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008caa30 — `GruntLogin_GetMatrixInfo`

- **Адрес (Offset):** `0x008caa30`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/GruntLogin.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008caa30
bool GruntLogin::GetMatrixInfo(uint32_t* width, uint32_t* height, uint32_t* minDigits, uint32_t* maxDigits, bool* flipCoords, uint32_t* challengeCount) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008caa30 в IDA Pro / Ghidra
