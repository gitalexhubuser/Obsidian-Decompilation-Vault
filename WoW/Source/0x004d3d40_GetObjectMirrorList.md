---
offset: "0x004d3d40"
module: "WoW/Source"
file: "WoW/Source/ObjectMgrClient/ObjectMgrClient.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004d3d40 — `GetObjectMirrorList`

- **Адрес (Offset):** `0x004d3d40`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/ObjectMgrClient/ObjectMgrClient.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004d3d40
static TSList<CMirrorHandler, TSGetLink<CMirrorHandler> >* GetObjectMirrorList(OBJECT_TYPE_ID typeId, CGObject_C* object, uint32_t index) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004d3d40 в IDA Pro / Ghidra
