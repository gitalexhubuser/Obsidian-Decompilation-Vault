---
offset: "0x004b9ea0"
module: "Engine/Source"
file: "Engine/Source/Services/AsyncFile.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x004b9ea0 — `AsyncFile_Cancel`

- **Адрес (Offset):** `0x004b9ea0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Services/AsyncFile.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004b9ea0
int32_t AsyncFile::Cancel(CAsyncObject* object, void (*callback)(CAsyncObject*)) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004b9ea0 в IDA Pro / Ghidra
