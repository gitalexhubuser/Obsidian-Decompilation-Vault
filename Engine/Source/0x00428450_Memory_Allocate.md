---
offset: "0x00428450"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Memory/MemoryStorm.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00428450 — `Memory_Allocate`

- **Адрес (Offset):** `0x00428450`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Memory/MemoryStorm.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00428450
void* Blizzard::Memory::Allocate(uint32_t bytes, uint32_t flags, const char* fileName, int32_t lineNumber) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00428450 в IDA Pro / Ghidra
