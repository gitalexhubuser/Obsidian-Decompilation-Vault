---
offset: "0x008a1440"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/HttpDownload.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008a1440 — `DownloadFileCallback_ReceivedData`

- **Адрес (Offset):** `0x008a1440`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/HttpDownload.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008a1440
bool DownloadFileCallback::ReceivedData(const void* data, int32_t size) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008a1440 в IDA Pro / Ghidra
