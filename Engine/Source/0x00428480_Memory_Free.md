---
offset: "0x00428480"
module: "Engine/Source"
file: "Engine/Source/BlizzardCore/Source/System/Memory/MemoryStorm.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00428480 — `Memory_Free`

- **Адрес (Offset):** `0x00428480`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/BlizzardCore/Source/System/Memory/MemoryStorm.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00428480
void Blizzard::Memory::Free(void* ptr, uint32_t flags, const char* fileName, int32_t lineNumber) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00428480 в IDA Pro / Ghidra
