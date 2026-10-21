---
offset: "0x006b9f70"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/FileDownload.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006b9f70 — `GruntFileDownload_CalculateMD5`

- **Адрес (Offset):** `0x006b9f70`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/FileDownload.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006b9f70
void STORMAPI GruntFileDownload::CalculateMD5(Storm::IOUnit* unit, uint64_t offset, uint64_t size, uint8_t* digest) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006b9f70 в IDA Pro / Ghidra
