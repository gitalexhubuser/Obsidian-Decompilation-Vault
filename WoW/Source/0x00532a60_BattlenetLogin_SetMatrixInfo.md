---
offset: "0x00532a60"
module: "WoW/Source"
file: "WoW/Source/WowServices/BattlenetLogin.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00532a60 — `BattlenetLogin_SetMatrixInfo`

- **Адрес (Offset):** `0x00532a60`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/BattlenetLogin.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00532a60
void BattlenetLogin::SetMatrixInfo(bool enabled, uint8_t width, uint8_t height, uint8_t minDigits, uint8_t maxDigits, bool flipCoords, uint8_t challengeCount, uint64_t seed, const uint8_t* sessionKey, uint32_t sessionKeyLength) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00532a60 в IDA Pro / Ghidra
