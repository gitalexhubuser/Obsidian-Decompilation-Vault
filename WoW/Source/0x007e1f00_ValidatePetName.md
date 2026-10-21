---
offset: "0x007e1f00"
module: "WoW/Source"
file: "WoW/Source/Game/ValidateName.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007e1f00 — `ValidatePetName`

- **Адрес (Offset):** `0x007e1f00`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Game/ValidateName.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007e1f00
VALIDATE_NAME_RESULT ValidatePetName(uint32_t language, const char* name, bool profanity, bool chatProfanity, bool reserved, bool english, uint32_t extraLength) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007e1f00 в IDA Pro / Ghidra
