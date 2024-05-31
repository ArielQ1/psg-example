habitats = {
    "polo norte": {
        "especies": {"oso polar", "morsa", "ballena"},
        "amenazas": ["cambio climático", "derretimiento de hielo", "contaminación"]
    },
    "amazonas": {
        "especies": {"tigre", "mono", "guacamayo"},
        "amenazas": ["deforestación", "caza furtiva", "pérdida de biodiversidad"]
    }
}
print(habitats)

habitats.update(
    arrecife_coral={
        "especies": {"pez payaso", "tortuga marina", "coral"},
        "amenazas": ["blanqueamiento de corales", "contaminación", "pesca excesiva"]
    },
    sabana_africana={
        "especies": {"elefante", "león", "rinoceronte"},
        "amenazas": ["caza furtiva", "pérdida de hábitat", "conflicto humano-vida silvestre"]
    }
)
print(habitats)

print('amazonas' in habitats)

habitats["amazonas"]["especies"].add("anaconda")
print(habitats)