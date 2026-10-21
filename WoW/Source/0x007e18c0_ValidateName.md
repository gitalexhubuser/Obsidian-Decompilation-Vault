---
offset: "0x007e18c0"
module: "WoW/Source"
file: "WoW/Source/Game/ValidateName.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007e18c0 — `ValidateName`

- **Адрес (Offset):** `0x007e18c0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Game/ValidateName.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007e18c0
VALIDATE_NAME_RESULT ValidateName(uint32_t language, const uint16_t* allowed, const char* name, uint32_t* length, int32_t* charset, bool profanity, bool chatProfanity, bool reserved, bool relaxed, bool english, int32_t charsetMask) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007e18c0 в IDA Pro / Ghidra
