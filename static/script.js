const cpuTemp = document.getElementById("cpu-temp");
const cpuPercent = document.getElementById("cpu-percent");
const cpuCores = document.getElementById("cpu-cores");

const ramTotal = document.getElementById("ram-total");
const ramUsed = document.getElementById("ram-used");
const ramPercent = document.getElementById("ram-percent");

const diskTotal = document.getElementById("disk-total");
const diskUsed = document.getElementById("disk-used");
const diskPercent = document.getElementById("disk-percent");

async function fetchStats() {
    const response = await fetch("/stats");
    const data = await response.json();

    cpuTemp.innerHTML = data.cpu.temp_celsius;
    cpuPercent.innerHTML = data.cpu.percent;
    cpuCores.innerHTML = data.cpu.cores;

    ramTotal.innerHTML = data.ram.total_gb;
    ramUsed.innerHTML = data.ram.used_gb;
    ramPercent.innerHTML = data.ram.percent;

    diskTotal.innerHTML = data.disk.total_gb;
    diskUsed.innerHTML = data.disk.used_gb;
    diskPercent.innerHTML = data.disk.percent;
}

setInterval(fetchStats, 2000);
fetchStats();