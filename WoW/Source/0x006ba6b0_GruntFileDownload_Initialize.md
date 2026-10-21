---
offset: "0x006ba6b0"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/FileDownload.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006ba6b0 — `GruntFileDownload_Initialize`

- **Адрес (Offset):** `0x006ba6b0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/FileDownload.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006ba6b0
bool GruntFileDownload::Initialize(const char* fileName, const uint8_t* md5, uint64_t size, uint64_t& offset) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006ba6b0 в IDA Pro / Ghidra
