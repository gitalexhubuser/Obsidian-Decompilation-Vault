---
offset: "0x00431db0"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/Packages/Mopaq/IOMpqUnit.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00431db0 — `IOMpqUnit_IOMpqUnit`

- **Адрес (Offset):** `0x00431db0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/Packages/Mopaq/IOMpqUnit.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00431db0
IOMpqUnit::IOMpqUnit(System_SFile::ARCHIVEREC* archive, const char* name, bool ownsMemory, IOUnit* next) : IOUnit(next, ownsMemory), m_position(0), m_archive(archive), m_name((name ? static_cast<uint32_t>(strlen(name)) : 0) + 1) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00431db0 в IDA Pro / Ghidra
