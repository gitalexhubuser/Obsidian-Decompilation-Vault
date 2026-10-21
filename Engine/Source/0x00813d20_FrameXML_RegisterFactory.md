---
offset: "0x00813d20"
module: "Engine/Source"
file: "Engine/Source/FrameXML/FrameXML.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00813d20 — `FrameXML_RegisterFactory`

- **Адрес (Offset):** `0x00813d20`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/FrameXML/FrameXML.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00813d20
int32_t FrameXML_RegisterFactory(const char* name, CSimpleFrame* (*factory)(CSimpleFrame* parent), bool unique) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00813d20 в IDA Pro / Ghidra
