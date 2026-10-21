---
offset: "0x004d8200"
module: "WoW/Source"
file: "WoW/Source/Glue/CGlueMgr.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004d8200 — `CGlueMgr_OnRealmSplitMsg`

- **Адрес (Offset):** `0x004d8200`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Glue/CGlueMgr.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004d8200
int32_t CGlueMgr::OnRealmSplitMsg(void* param, NETMESSAGE msgId, uint32_t time, CDataStore* msg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004d8200 в IDA Pro / Ghidra
