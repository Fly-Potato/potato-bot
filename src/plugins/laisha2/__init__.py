from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import httpx
import json

material = on_command("材料", rule=to_me(), priority=5)


@material.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()  # 首次发送时的参数
    if args:
        state['name'] = args


@material.got('name', prompt="请输入想查询的材料名称")
async def handle_name(bot: Bot, event: Event, state: T_State):
    name = state['name']
    material_list = await get_material(name)
    for material_info in material_list:
        await material.send(material_info)
    await material.finish()


async def get_material(name: str):
    async with httpx.AsyncClient() as client:
        res = await client.get(f"http://127.0.0.1:8002/botdata/laisha2/material/?name={name}")
        material_list = list()
        for material_info in json.loads(res.text)['materials']:
            material_list.append(f"名称:{material_info['name']}, 类型: {material_info['type']}, 地区:{material_info['addr']}")
    return material_list
