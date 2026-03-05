#!/usr/bin/env python3
"""
XHS Card Templates Renderer
用法: python3 render.py --style warm --type cover --output /path/to/output.png --html /path/to/template.html
或者直接传入 HTML 文件路径渲染。
"""
import asyncio
import argparse
import os
import sys
from playwright.async_api import async_playwright

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(SKILL_DIR, "assets", "templates")

STYLES = ["warm", "dark", "bw", "blue", "pink"]
CARD_TYPES = {
    "warm": ["cover", "card_list", "card_text", "card_quote"],
    "dark": ["cover"],
    "bw": ["cover"],
    "blue": ["cover"],
    "pink": ["cover"],
}


async def render_html(html_path: str, output_path: str, width: int = 1080, height: int = 1440):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": width, "height": height})
        await page.goto(f"file://{os.path.abspath(html_path)}")
        await page.wait_for_timeout(1500)
        await page.screenshot(
            path=output_path,
            clip={"x": 0, "y": 0, "width": width, "height": height}
        )
        await browser.close()
    print(f"✅ Rendered: {output_path}")


async def render_style(style: str, output_dir: str):
    style_dir = os.path.join(TEMPLATES_DIR, style)
    os.makedirs(output_dir, exist_ok=True)
    cards = CARD_TYPES.get(style, ["cover"])
    for card in cards:
        html = os.path.join(style_dir, f"{card}.html")
        if os.path.exists(html):
            out = os.path.join(output_dir, f"{style}_{card}.png")
            await render_html(html, out)
        else:
            print(f"⚠️  Not found: {html}")


async def main():
    parser = argparse.ArgumentParser(description="Render XHS card templates")
    parser.add_argument("--style", choices=STYLES + ["all"], default="warm",
                        help="风格: warm / dark / bw / blue / pink / all")
    parser.add_argument("--html", help="直接指定 HTML 文件路径渲染")
    parser.add_argument("--output", default="/tmp/xhs_output", help="输出目录或文件路径")
    args = parser.parse_args()

    if args.html:
        out = args.output if args.output.endswith(".png") else os.path.join(args.output, "output.png")
        os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
        await render_html(args.html, out)
    elif args.style == "all":
        for style in STYLES:
            await render_style(style, args.output)
    else:
        await render_style(args.style, args.output)


if __name__ == "__main__":
    asyncio.run(main())
