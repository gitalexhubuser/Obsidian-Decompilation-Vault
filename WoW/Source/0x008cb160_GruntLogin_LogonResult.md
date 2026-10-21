---
offset: "0x008cb160"
module: "WoW/Source"
file: "WoW/Source/WowServices/GruntLogin.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008cb160 — `GruntLogin_LogonResult`

- **Адрес (Offset):** `0x008cb160`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/GruntLogin.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008cb160
void GruntLogin::LogonResult(Grunt::Result result, const uint8_t* sessionKey, uint32_t sessionKeyLength, uint16_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008cb160 в IDA Pro / Ghidra
