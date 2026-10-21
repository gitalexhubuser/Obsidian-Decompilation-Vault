---
offset: "0x00812840"
module: "Engine/Source"
file: "Engine/Source/FrameXML/FrameXML.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00812840 — `FrameXML_RegisterLoadProgressCallback`

- **Адрес (Offset):** `0x00812840`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/FrameXML/FrameXML.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00812840
void FrameXML_RegisterLoadProgressCallback(void (*callback)(float progress, void* param), void* param, uint32_t total) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00812840 в IDA Pro / Ghidra
