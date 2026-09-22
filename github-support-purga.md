# Solicitud a GitHub Support: purgar commits inalcanzables

Los commits viejos ya no los apunta ninguna rama ni etiqueta, pero GitHub los sigue
sirviendo por su SHA directo hasta que hace limpieza interna. Esto se lo pides a Soporte.

**Dónde:** https://support.github.com/request → categoría *Account or profile* →
asunto *Remove sensitive data from repository*. Hay que enviarlo con la cuenta `operonte`.

---

## Asunto

    Purge unreachable commits containing sensitive data (6 repositories)

## Mensaje

> Hello,
>
> I rewrote the history of the repositories below with `git filter-repo` to remove
> sensitive data, and force-pushed both branches and tags. No branch or tag points to
> the old commits any more, but they are still reachable by their direct SHA.
>
> Could you please run garbage collection on these repositories so the unreachable
> objects are removed, and clear any cached views of them?
>
> - operonte/acceso — removed hardcoded credentials (e.g. commit `6aa84c1`)
> - operonte/Holyapp — removed Firebase API keys
> - operonte/preciobencina — removed Firebase API keys
> - operonte/coroapp — removed Firebase API keys and committed APK files
> - operonte/misionapp — removed Firebase API keys and committed APK files
> - operonte/sosapp — removed Firebase API keys
>
> All six repositories are public and I am the owner. There are no forks.
>
> Thank you,
> Cristian Bravo (operonte)

---

## Después de que respondan

Comprobar que el commit ya no existe:

    curl -s -o /dev/null -w "%{http_code}\n" \
      https://api.github.com/repos/operonte/acceso/commits/6aa84c1

`404` significa que se purgó. Mientras devuelva `200`, sigue accesible.

## Lo que esto NO cubre

Los APK publicados en las releases llevan las claves dentro y cualquiera puede
descomprimirlos. Eso solo se resuelve republicando esas versiones, o asumiendo que
esas claves son conocidas.
