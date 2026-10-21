---
offset: "0x006baf10"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/FileDownload.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006baf10 — `BattlenetFileDownload_Initialize`

- **Адрес (Offset):** `0x006baf10`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/FileDownload.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006baf10
bool BattlenetFileDownload::Initialize(const char* fileName, const uint8_t* md5, uint64_t size, uint64_t& offset) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006baf10 в IDA Pro / Ghidra
