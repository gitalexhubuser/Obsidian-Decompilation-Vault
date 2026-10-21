---
offset: "0x00428b00"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Unicode/Unicode.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00428b00 — `Unicode_ConvertUTF8to16`

- **Адрес (Offset):** `0x00428b00`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Unicode/Unicode.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00428b00
int32_t Blizzard::Unicode::ConvertUTF8to16(uint16_t* dst, uint32_t dstmaxchars, const char* src, int32_t srcmaxchars, uint32_t* dstchars, uint32_t* srcchars) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00428b00 в IDA Pro / Ghidra
