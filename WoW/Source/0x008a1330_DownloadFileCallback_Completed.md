---
offset: "0x008a1330"
module: "WoW/Source"
file: "WoW/Source/WowSvcs/WowSvcsClient/HttpDownload.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x008a1330 — `DownloadFileCallback_Completed`

- **Адрес (Offset):** `0x008a1330`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowSvcs/WowSvcsClient/HttpDownload.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008a1330
void DownloadFileCallback::Completed(Blizzard::URL::DownloadCallback::Status status) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008a1330 в IDA Pro / Ghidra
