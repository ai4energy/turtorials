<template>
  <div style="max-width:860px;margin:32px auto;font-family:'Source Han Sans CN',sans-serif;">
    <h2>Vue 3 单文件组件任务看板 · FastAPI 后端联调</h2>
    <p>后端健康状态：<strong>{{ healthText }}</strong></p>
    <div style="display:flex;gap:8px;margin-bottom:14px;">
      <input v-model="newTitle" placeholder="输入学习任务" style="flex:1;padding:8px 12px;" />
      <select v-model="newCat" style="padding:8px;">
        <option>Docker</option><option>FastAPI</option><option>Vue</option><option>Nginx</option>
      </select>
      <button @click="addTask">添加任务</button>
    </div>
    <div v-for="t in tasks" :key="t.id" style="display:flex;justify-content:space-between;padding:10px;border:1px solid #cbd5e1;margin-bottom:8px;border-radius:8px;">
      <span>[{{ t.category }}] {{ t.title }}</span>
      <button @click="toggleTask(t.id)">{{ t.done ? '已完成' : '标记完成' }}</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
const tasks = ref([])
const healthText = ref('检测中...')
const newTitle = ref('')
const newCat = ref('FastAPI')

async function loadAll() {
  const h = await fetch('/api/health').then(r => r.json())
  healthText.value = `${h.status} (${h.service})`
  const d = await fetch('/api/tasks').then(r => r.json())
  tasks.value = d.items || []
}
async function addTask() {
  if (!newTitle.value.trim()) return
  await fetch('/api/tasks', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title: newTitle.value.trim(), category: newCat.value })
  })
  newTitle.value = ''
  await loadAll()
}
async function toggleTask(id) {
  await fetch(`/api/tasks/${id}/toggle`, { method: 'POST' })
  await loadAll()
}
onMounted(loadAll)
</script>
