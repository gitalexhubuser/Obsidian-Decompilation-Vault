---
offset: "0x008cad40"
module: "WoW/Source"
file: "WoW/Source/WowServices/GruntLogin.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008cad40 — `GruntLogin_SetMatrixInfo`

- **Адрес (Offset):** `0x008cad40`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/GruntLogin.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008cad40
void GruntLogin::SetMatrixInfo(bool enabled, uint8_t width, uint8_t height, uint8_t minDigits, uint8_t maxDigits, bool flipCoords, uint8_t challengeCount, uint64_t seed, const uint8_t* sessionKey, uint32_t sessionKeyLength) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008cad40 в IDA Pro / Ghidra
