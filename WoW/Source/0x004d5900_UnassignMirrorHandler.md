---
offset: "0x004d5900"
module: "WoW/Source"
file: "WoW/Source/ObjectMgrClient/ObjectMgrClient.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004d5900 — `UnassignMirrorHandler`

- **Адрес (Offset):** `0x004d5900`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/ObjectMgrClient/ObjectMgrClient.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004d5900
static void UnassignMirrorHandler(TSList<CMirrorHandler, TSGetLink<CMirrorHandler> >* list, MIRRORHANDLERFUNC function, void* param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004d5900 в IDA Pro / Ghidra
