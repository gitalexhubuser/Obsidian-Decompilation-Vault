---
offset: "0x00428940"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Unicode/Unicode.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00428940 — `Unicode_ConvertUTF16to8`

- **Адрес (Offset):** `0x00428940`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Unicode/Unicode.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00428940
int32_t Blizzard::Unicode::ConvertUTF16to8(char* dst, uint32_t dstmaxchars, const uint16_t* src, int32_t srcmaxchars, uint32_t* dstchars, uint32_t* srcchars) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00428940 в IDA Pro / Ghidra
