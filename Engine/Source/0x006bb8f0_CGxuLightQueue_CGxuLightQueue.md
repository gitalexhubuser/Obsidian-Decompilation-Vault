---
offset: "0x006bb8f0"
module: "Engine/Source"
file: "Engine/Source/Gxu/GxuLight.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x006bb8f0 — `CGxuLightQueue_CGxuLightQueue`

- **Адрес (Offset):** `0x006bb8f0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Gxu/GxuLight.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006bb8f0
CGxuLightQueue::CGxuLightQueue(const uint32_t (&params)[2]) : CMemBlock(sizeof(CGxuLight*) * params[0], 0, typeid(CGxuLight*).raw_name(), SLOG_OBJECT) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006bb8f0 в IDA Pro / Ghidra
