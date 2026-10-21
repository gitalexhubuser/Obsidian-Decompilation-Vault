---
offset: "0x004a8e80"
module: "Engine/Source"
file: "Engine/Source/Images/ImageWriter.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004a8e80 — `ImageWriterInitialize`

- **Адрес (Offset):** `0x004a8e80`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Images/ImageWriter.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004a8e80
int32_t ImageWriterInitialize(uint32_t dataSize, void* (*allocFunc)(size_t bytes), void (*freeFunc)(void* ptr), int32_t flags) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004a8e80 в IDA Pro / Ghidra
