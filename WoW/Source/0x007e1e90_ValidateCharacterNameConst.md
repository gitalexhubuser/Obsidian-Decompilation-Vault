---
offset: "0x007e1e90"
module: "WoW/Source"
file: "WoW/Source/Game/ValidateName.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x007e1e90 — `ValidateCharacterNameConst`

- **Адрес (Offset):** `0x007e1e90`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Game/ValidateName.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x007e1e90
VALIDATE_NAME_RESULT ValidateCharacterNameConst(uint32_t language, const char* name, bool profanity, bool chatProfanity, bool reserved, bool english, int32_t extraLength) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x007e1e90 в IDA Pro / Ghidra
