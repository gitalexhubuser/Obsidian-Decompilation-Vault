---
offset: "0x008cb020"
module: "WoW/Source"
file: "WoW/Source/WowServices/GruntLogin.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008cb020 — `GruntLogin_ReconnectResult`

- **Адрес (Offset):** `0x008cb020`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/GruntLogin.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008cb020
void GruntLogin::ReconnectResult(Grunt::Result result, const uint8_t* sessionKey, uint32_t sessionKeyLength, uint16_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008cb020 в IDA Pro / Ghidra
