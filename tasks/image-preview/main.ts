import type { Context } from "@oomol/types/oocana";

type Inputs = {
  image: string;
}
type Outputs = {
  output: unknown;
}

export default async function(
  params: Inputs,
  context: Context<Inputs, Outputs>
): Promise<Outputs> {
  context.preview({
    type: "image",
    data: params.image,
  })
  return { output: null };
};
