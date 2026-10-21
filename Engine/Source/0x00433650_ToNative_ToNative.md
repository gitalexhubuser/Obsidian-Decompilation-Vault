---
offset: "0x00433650"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Unicode/Win64/Unicode.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00433650 — `ToNative_ToNative`

- **Адрес (Offset):** `0x00433650`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Unicode/Win64/Unicode.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00433650
Blizzard::StringConversion_CodepageToUTF8::ToNative::ToNative(const char* str) : Blizzard::Memory::TempBuffer<char, 300>((str ? static_cast<uint32_t>(strlen(str)) : 0) + 1) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00433650 в IDA Pro / Ghidra
