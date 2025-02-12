import { Client } from "@notionhq/client";
import {
  CreatePageParameters,
  UpdatePageParameters,
} from "@notionhq/client/build/src/api-endpoints";

if (!process.env.NOTION_TOKEN) {
  throw new Error("Missing NOTION_TOKEN environment variable");
}

const notion = new Client({
  auth: process.env.NOTION_TOKEN,
});

export async function getDatabase(databaseId: string) {
  return notion.databases.query({
    database_id: databaseId,
  });
}

export async function getPage(pageId: string) {
  return notion.pages.retrieve({
    page_id: pageId,
  });
}

export type NotionProperties = {
  [key: string]: {
    type: string;
    [key: string]: unknown;
  };
};

export async function createPage(
  databaseId: string,
  properties: CreatePageParameters["properties"]
) {
  return notion.pages.create({
    parent: { database_id: databaseId },
    properties,
  });
}

export async function updatePage(
  pageId: string,
  properties: UpdatePageParameters["properties"]
) {
  return notion.pages.update({
    page_id: pageId,
    properties,
  });
}
