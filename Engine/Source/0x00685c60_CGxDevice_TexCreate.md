---
offset: "0x00685c60"
module: "Engine/Source"
file: "Engine/Source/Gx/CGxDevice/CGxDevice.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00685c60 — `CGxDevice_TexCreate`

- **Адрес (Offset):** `0x00685c60`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Gx/CGxDevice/CGxDevice.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00685c60
int32_t CGxDevice::TexCreate(EGxTexTarget target, uint32_t width, uint32_t height, uint32_t depth, EGxTexFormat format, EGxTexFormat dataFormat, CGxTexFlags flags, void* userArg, GxTexUserFunc userFunc, const char* name, CGxTex*& texId) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00685c60 в IDA Pro / Ghidra
