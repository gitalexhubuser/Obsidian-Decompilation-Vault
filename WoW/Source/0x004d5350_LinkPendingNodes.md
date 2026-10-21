---
offset: "0x004d5350"
module: "WoW/Source"
file: "WoW/Source/ObjectMgrClient/ObjectMgrClient.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004d5350 — `LinkPendingNodes`

- **Адрес (Offset):** `0x004d5350`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/ObjectMgrClient/ObjectMgrClient.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004d5350
static int32_t LinkPendingNodes(TSExplicitList<CMirrorHandler, offsetof(CMirrorHandler, m_link2)>* pending, TSList<CMirrorHandler, TSGetLink<CMirrorHandler> >* list) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004d5350 в IDA Pro / Ghidra
