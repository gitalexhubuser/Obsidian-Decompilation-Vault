---
offset: "0x004d7890"
module: "WoW/Source"
file: "WoW/Source/Glue/CGlueMgr.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004d7890 — `CGlueMgr_ServerAlertURLCallback`

- **Адрес (Offset):** `0x004d7890`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Glue/CGlueMgr.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004d7890
bool CGlueMgr::ServerAlertURLCallback(void* param, const char* data, uint32_t size, bool done, HTTPError::ErrorCode error) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004d7890 в IDA Pro / Ghidra
