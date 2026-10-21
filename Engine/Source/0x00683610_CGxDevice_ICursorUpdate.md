---
offset: "0x00683610"
module: "Engine/Source"
file: "Engine/Source/Gx/CGxDevice/CGxDevice.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00683610 — `CGxDevice_ICursorUpdate`

- **Адрес (Offset):** `0x00683610`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Gx/CGxDevice/CGxDevice.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00683610
void CGxDevice::ICursorUpdate(EGxTexCommand command, uint32_t width, uint32_t height, uint32_t face, uint32_t level, void* userArg, uint32_t& texelStrideInBytes, const void*& texels) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00683610 в IDA Pro / Ghidra
